<template>
    <div>
        <button v-show="leftshow">{{ left }}</button>
        aa-{{ title }}
        <button v-show="rightshow">{{ right }}</button>
    </div>
</template>

<script>
export default {
    // props: ["title", "left", "right", "leftshow", "rightshow"]
    // 禁止透传
    inheritAttrs: false,
    props: {
        title: String,
        left: [String, Number],
        right: {
            // 要求是否必填
            required: true,
            type: String,
            validator(value){
                return ['success', 'warning', 'danger'].includes(value)
            }
        },
        leftshow: Boolean,
        rightshow: {
            type: Boolean,
            // 默认值
            default: true
        }
    }
}
</script>

<style scoped></style>

