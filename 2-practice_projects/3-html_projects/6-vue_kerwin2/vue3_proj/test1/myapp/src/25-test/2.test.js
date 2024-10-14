import { describe, test, expect } from 'vitest'
import useTabbarStore from '../24-pinia/store/tabbarStore'
import { setActivePinia, createPinia } from 'pinia'
import { beforeAll } from 'vitest'

describe('测试store', () => {
    let store
    let cinemaStore
    beforeAll(async () => {
        // 显式的激活pinia
        setActivePinia(createPinia())
        const useCinemaStore = await import('../24-pinia/store/cinemaStore')
        console.log(useCinemaStore.default);
        store = useTabbarStore()
        cinemaStore = useCinemaStore.default()
    })
    test('测试1：测试tabbarStore', () => {
        // 使用store
        expect(store.isTabbarShow).toBe(true)
        store.change(false)
        expect(store.isTabbarShow).toBe(false)
    })
    test('测试2：测试cenimaStore', async () => {
        expect(cinemaStore.cinemaList.length).toBe(0)
        await cinemaStore.getCinemaList()
        expect(cinemaStore.cinemaList.length).gt(0)
    })
})