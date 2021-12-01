#!/usr/bin/env python
# -*- coding: utf-8 -*-

arr = [int(x) for x in open('input.txt').readlines()]


def part1():
    count = 0

    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            count += 1

    print(count)


def part2():
    count = 0

    for i in range(2, len(arr) - 1):
        sum1 = arr[i]+arr[i-1]+arr[i-2]
        sum2 = arr[i+1]+arr[i]+arr[i-1]
        if sum2 > sum1:
            count += 1

    print(count)


part1()
part2()
