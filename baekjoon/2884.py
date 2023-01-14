h, m = [int(x) for x in input().split()]
alarm = h * 60 + m - 45
if alarm < 0: alarm = 24 * 60 + alarm
print(alarm // 60, alarm % 60)