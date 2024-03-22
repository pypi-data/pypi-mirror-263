# Python IEC62056 Meter Tools

## How to use ?

### Install

```shell
pip install py-iec62056
```

### Create SerialClient

```python
client = SerialClient(
    baudrate=19200,
    port="COM3",
    transport="serial",
    parity="E",
    bytesize=7,
    stopbits=1
)
```

### Read A meter identification

This return an identification message from the meter.
You must set the ack_stop to True if you don't want to meter to give the default table.

```python
result = client.read_tariff_identification("5987893", ack_stop=True)
```

### Read Table dataset

This will return a list of DataSet instance.
Raise error if Timeout.

```python
result = client.request(meter_address="5987893", table=7, timeout=30)
assert isinstance(result, TariffResponse)
for dataset in result.data:
    logging.info(f"{dataset}")
```
