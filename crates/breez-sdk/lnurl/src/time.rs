use std::time::SystemTime;

pub fn now() -> i64 {
    SystemTime::now()
        .duration_since(SystemTime::UNIX_EPOCH)
        .expect("Time went backwards")
        .as_secs()
        .try_into()
        .expect("SystemTime overflow")
}
