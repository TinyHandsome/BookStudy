<template>
  <div>
    <button @click="handleLeft">left</button>
    myname
    <button v-show="myright">right</button>

    <slot></slot>
  </div>
</template>

<script>
export default {
  // props: ['myname', 'myright']
  props: {
    myname: {
      type: String,
      default: "",
    },
    myright: {
      type: Boolean,
      default: true,
    },
  },
  methods: {
    handleLeft() {
      this.$emit("event");
    },
  },
};
</script>
