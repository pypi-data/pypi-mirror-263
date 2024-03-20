import pyarrow as pa
import pyarrow.flight as fl
import os


def sample(host=None):
    """Returns a data sample for machine learning."""
    if host is None:
        host = os.environ.get("HOST", None)
    if host is None:
        raise Exception(
            "The flight server host must be either passed as the `host` argument or set in the `HOST` environment variable."
        )
    client = pa.flight.connect(os.environ.get("HOST", ""))
    reader = client.do_get(fl.Ticket("sample"))
    flight_data = reader.read_all()
    data = flight_data.to_pandas()
    data_genuine = data.iloc[:, data.columns != "Fraud"]
    data_fraud = data["Fraud"].astype("int")

    return data_genuine, data_fraud
