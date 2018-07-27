<template>
    <weight_graph :chartData="datum"/>
</template>

<script>
    import weight_graph from './graphs/weight_graph.vue'

    export default {
        props: [],
        components: {
            weight_graph
        },
        data: function () {
            return { 
                datum: { }
        },
        methods: {
            getWeightLog: function () {
                alert('send request for data');
                // Placeholder data
                this.datum = {
                    labels: ['2018-05-05', '2018-05-06', '2018-05-07', '2018-05-08'],
                    datasets: [
                        {
                            label: 'Weight',
                            backgroundColor: '#f3f3f3',
                            data: [1, 2, 1, 1]
                        }
                    ]
                }
            }
        }
    }
</script>
