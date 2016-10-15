from rapidconnect import RapidConnect

ml = RapidConnect("test", "test2")

result = ml.call("packages", "block", "params")

print result
