use std::ops::BitOr;

use polars_core::prelude::*;
use polars_core::utils::try_get_supertype;
use polars_error::polars_ensure;

use crate::frame::join::*;
use crate::prelude::*;

pub fn replace(
    s: &Series,
    old: &Series,
    new: &Series,
    default: &Series,
    return_dtype: Option<DataType>,
) -> PolarsResult<Series> {
    polars_ensure!(
        old.n_unique()? == old.len(),
        ComputeError: "`old` input for `replace` must not contain duplicates"
    );

    let return_dtype = match return_dtype {
        Some(dtype) => dtype,
        None => try_get_supertype(new.dtype(), default.dtype())?,
    };

    polars_ensure!(
        default.len() == s.len() || default.len() == 1,
        ComputeError: "`default` input for `replace` must have the same length as the input or have length 1"
    );

    let default = default.cast(&return_dtype)?;

    if old.len() == 0 {
        let out = if default.len() == 1 && s.len() != 1 {
            default.new_from_index(0, s.len())
        } else {
            default
        };

        return Ok(out);
    }

    let old = match (s.dtype(), old.dtype()) {
        #[cfg(feature = "dtype-categorical")]
        (DataType::Categorical(_, ord), DataType::String) => {
            let dt = DataType::Categorical(None, *ord);
            old.strict_cast(&dt)?
        },
        _ => old.strict_cast(s.dtype())?,
    };
    let new = new.cast(&return_dtype)?;

    if new.len() == 1 {
        replace_by_single(s, &old, &new, &default)
    } else {
        replace_by_multiple(s, old, new, &default)
    }
}

// Fast path for replacing by a single value
fn replace_by_single(
    s: &Series,
    old: &Series,
    new: &Series,
    default: &Series,
) -> PolarsResult<Series> {
    let mask = if old.null_count() == old.len() {
        s.is_null()
    } else {
        let mask = is_in(s, old)?;

        if old.null_count() == 0 {
            mask
        } else {
            mask.bitor(s.is_null())
        }
    };
    new.zip_with(&mask, default)
}

/// General case for replacing by multiple values
fn replace_by_multiple(
    s: &Series,
    old: Series,
    new: Series,
    default: &Series,
) -> PolarsResult<Series> {
    polars_ensure!(
        new.len() == old.len(),
        ComputeError: "`new` input for `replace` must have the same length as `old` or have length 1"
    );

    let df = s.clone().into_frame();
    let replacer = create_replacer(old, new)?;

    let joined = df.join(
        &replacer,
        [s.name()],
        ["__POLARS_REPLACE_OLD"],
        JoinArgs {
            how: JoinType::Left,
            join_nulls: true,
            ..Default::default()
        },
    )?;

    let replaced = joined.column("__POLARS_REPLACE_NEW").unwrap();

    if replaced.null_count() == 0 {
        return Ok(replaced.clone());
    }

    match joined.column("__POLARS_REPLACE_MASK") {
        Ok(col) => {
            let mask = col.bool().unwrap();
            replaced.zip_with(mask, default)
        },
        Err(_) => {
            let mask = &replaced.is_not_null();
            replaced.zip_with(mask, default)
        },
    }
}

// Build replacer dataframe
fn create_replacer(mut old: Series, mut new: Series) -> PolarsResult<DataFrame> {
    old.rename("__POLARS_REPLACE_OLD");
    new.rename("__POLARS_REPLACE_NEW");

    let cols = if new.null_count() > 0 {
        let mask = Series::new("__POLARS_REPLACE_MASK", &[true]).new_from_index(0, new.len());
        vec![old, new, mask]
    } else {
        vec![old, new]
    };
    let out = unsafe { DataFrame::new_no_checks(cols) };
    Ok(out)
}
