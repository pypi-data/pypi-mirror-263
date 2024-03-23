use pyo3::prelude::*;

pub mod aio;
pub mod exceptions;
pub mod json;
pub mod py2rs;
pub mod rs2py;

#[pymodule]
fn rust_requests(py: Python, module: &PyModule) -> PyResult<()> {
    aio::init_module(py, module, module)?;
    rs2py::init_module(py, module, module)?;
    exceptions::init_module(py, module, module)?;
    Ok(())
}
