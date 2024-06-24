import Counter from './App.vue'
import Child from './Child.vue'
import { render, fireEvent } from '@testing-library/vue'

import { describe, test, expect } from 'vitest'

describe('组件测试', () => {
    test('测试1：测试App组件', async () => {
        const { getByText } = render(Counter)
        getByText("0")  // 隐式测试

        const button = getByText("add")
        await fireEvent.click(button)
        getByText("1")
    })

    test('测试2：测试App组件的孩子组件', async () => {
        const { getByText } = render(Child, {
            props: {
                title: "kerwin"
            }
        })
        getByText("kerwin")  // 隐式测试

    })
})