#![allow(dead_code)]

use pyo3::prelude::*;
use minify_js::{Session, TopLevelMode, minify};
use pyo3::exceptions::PyValueError;

/// A Python module implemented in Rust. The name of this function must match
/// the `lib.name` setting in the `Cargo.toml`, else Python will not be able to
/// import the module.
#[pymodule]
fn jsminify_rs(_: Python<'_>, m: &PyModule) -> PyResult<()> {
    /// Minifies the input string
    #[pyfn(m)]
    fn minify_string(code: String) -> PyResult<String> {
        let code = code.as_bytes();
        let session = Session::new();
        let mut out = Vec::new();

        match minify(&session, TopLevelMode::Global, code, &mut out) {
            Ok(_) => (),
            Err(e) => return Err(PyValueError::new_err(e.to_string())),
        };

        return match String::from_utf8(out) {
            Ok(s) => Ok(s),
            Err(_) => Err(PyValueError::new_err("Invalid UTF-8 sequence")),
        };
    }

    Ok(())
}