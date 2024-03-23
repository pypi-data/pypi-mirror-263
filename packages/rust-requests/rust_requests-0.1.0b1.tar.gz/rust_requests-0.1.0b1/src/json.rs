use std::collections::HashMap;

use serde::{Deserialize, Serialize};

use colored_json::prelude::*;
use pyo3::exceptions::{PyIndexError, PyKeyError, PyTypeError};
use pyo3::prelude::*;

#[derive(Debug, Clone, FromPyObject, Serialize, Deserialize)]
#[serde(untagged)]
pub enum PySerde {
    Object(HashMap<String, PySerde>),
    Boolean(bool),
    Number(isize),
    Float(f64),
    String(String),
    Null(Option<isize>),
    Array(Vec<PySerde>),
}

impl ToPyObject for PySerde {
    fn to_object(&self, py: Python<'_>) -> PyObject {
        match self {
            Self::Null(_) => Option::<isize>::None.to_object(py),
            Self::Boolean(inner) => inner.to_object(py),
            Self::String(inner) => inner.to_object(py),
            Self::Float(inner) => inner.to_object(py),
            Self::Number(inner) => inner.to_object(py),
            Self::Array(inner) => {
                let mut new_holder = vec![];
                for item in inner {
                    new_holder.push(item.to_object(py));
                }
                new_holder.to_object(py)
            }
            Self::Object(inner) => {
                let mut new_holder = HashMap::new();
                for (key, elem) in inner {
                    new_holder.insert(key, elem.to_object(py));
                }
                new_holder.to_object(py)
            }
        }
    }
}

#[derive(Debug, FromPyObject)]
pub enum PyIndex {
    Int(usize),
    Str(String),
}

#[derive(Clone)]
#[pyclass(module = "rust_requests")]
pub struct LazyJSON(pub PySerde);

impl LazyJSON {
    pub fn access_at<'rt>(&'rt self, keys: Vec<PyIndex>) -> PyResult<&'rt PySerde> {
        let mut current_value = &self.0;
        for field in keys {
            match current_value {
                PySerde::Object(object) => match field {
                    PyIndex::Int(index) => {
                        return Err(PyTypeError::new_err(format!(
                            r#"Cannot access the index ({})
                                    because accessible is an object with string keys"#,
                            index
                        )))
                    }
                    PyIndex::Str(index) => match object.get(index.as_str()) {
                        None => {
                            return Err(PyKeyError::new_err(format!("No such key: {}", &index)))
                        }
                        Some(new_value) => current_value = new_value,
                    },
                },
                PySerde::Array(array) => match field {
                    PyIndex::Str(index) => {
                        return Err(PyTypeError::new_err(format!(
                            r#"Cannot access the key ({})
                                    because accessible is an array"#,
                            index
                        )))
                    }
                    PyIndex::Int(index) => match array.get(index) {
                        None => {
                            return Err(PyIndexError::new_err(format!(
                                "Index out of length: {} (length is {})",
                                &index,
                                array.len()
                            )))
                        }
                        Some(new_value) => current_value = new_value,
                    },
                },
                _ => return Err(PyTypeError::new_err("Accessible is not subscriptable")),
            };
        }
        Ok(current_value)
    }
}

#[pymethods]
impl LazyJSON {
    #[args(keys = "*")]
    pub fn query(&self, keys: Vec<PyIndex>) -> PyResult<PyObject> {
        let mapping = self.access_at(keys)?;
        Ok(Python::with_gil(|py| mapping.to_object(py)))
    }

    #[args(keys = "*")]
    pub fn show(&self, keys: Vec<PyIndex>) -> PyResult<()> {
        let mapping = self.access_at(keys)?;
        let colored = serde_json::to_string(mapping)
            .unwrap()
            .to_colored_json_auto()
            .unwrap();
        println!("{}", colored);
        Ok(())
    }
}
