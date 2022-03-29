
# modelop.score
def action(datum):
  print("action datum:", flush=True)
  print(datum, flush=True)
  yield {
    "foo": 1,
    "bar": "score"
  }

# modelop.metrics
def metrics_one(datum):
  print("metrics_one datum:", flush=True)
  print(datum, flush=True)
  yield {
    "foo": 1,
    "bar": "test result"
  }

def metrics_two(datumA, datumB):
  print("metrics_two datumA:", flush=True)
  print(datumA, flush=True)
  print("metrics_two datumB:", flush=True)
  print(datumB, flush=True)
  yield {
    "foo": 2,
    "bar": "test result"
  }

def metrics_three(datumA, datumB, datumC):
  print("metrics_three datumA:", flush=True)
  print(datumA, flush=True)
  print("metrics_three datumB:", flush=True)
  print(datumB, flush=True)
  print("metrics_three datumC:", flush=True)
  print(datumC, flush=True)
  yield {
    "foo": 3,
    "bar": "test result"
  }

# modelop.train
def train_one(datum):
  print("train_one datum:", flush=True)
  print(datum, flush=True)
  yield {
    "foo": 1,
    "bar": "training"
  }
