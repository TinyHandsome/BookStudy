<template>
    <div>
        <button @click="handleShow">left</button>
        navbar -- {{ myname }}
        <button>right</button>
    </div>
</template>

<script>
export default {
    props: ["myname", "myid"],
    mounted() {
        console.log("222", this.myid);
    },

    setup(props, { emit }) {
        console.log(props.myid);

        const handleShow = () => {
            emit("event")
        }

        return {
            handleShow
        }
    }
}
</script>