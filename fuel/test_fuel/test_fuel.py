from fuel.fuel import gauge, convert

def test_convert():
  assert convert("0/1") == 0
  assert convert("3/4") == 75
  assert convert("4/4") == "1"

def test_gauge():
  assert gauge("4/4") == "F"
  assert gauge("0/1") == "E"
  assert gauge("3/4") == "75%"
