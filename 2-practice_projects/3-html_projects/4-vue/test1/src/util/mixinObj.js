const obj = {
    created() {
        this.$store.commit("hide");
    },
    destroyed() {
        this.$store.commit("show");
    },
    methods: {
        a() {
            console.log("aaa");
        },
    },
};

export default obj