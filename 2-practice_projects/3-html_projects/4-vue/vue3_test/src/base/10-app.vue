<template>
    <div>
        app
        <ul>
            <li v-for="data in obj1.list" :key="data.name">
                {{ data.name }}
            </li>
        </ul>
        <ul>
            <li v-for="data in obj2.list" :key="data.name">
                {{ data.name }}
            </li>
        </ul>
    </div>
</template>

<script>
import { getData1, getData2 } from './module/app'

export default {
    setup() {
        const obj1 = getData1()
        const obj2 = getData2()

        return {
            obj1,
            obj2
        }
    }
}
</script>