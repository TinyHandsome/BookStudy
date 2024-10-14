import { increment } from './moduleA'
import { describe, test, expect } from 'vitest'

describe('测试increment方法', () => {
    test('测试1：increments the current number by 1', () => {
        expect(increment(0, 10)).toBe(1)
    })

    test('测试2：does not increment the current number over the max', () => {
        expect(increment(10, 10)).toBe(10)
    })

    test('测试3：has a default max of 10', () => {
        expect(increment(10)).toBe(10)
    })
})