<template>
        <line_graph :chartData="datum" :style="graph_style"/>
</template>

<script>
    import line_graph from './graphs/line_graph.vue'
    import modal from './modal.vue'
    import axios from 'axios'

    export default {
        props: [],
        components: {
            line_graph,
            modal
        },
        data: function () {
            return { 
                datum: {
                    labels: ['2018-05-05', '2018-05-06', '2018-05-07', '2018-05-08'],
                    datasets: [
                        {
                            label: 'Calories In',
                            backgroundColor: '#f3f3f3',
                            data: [1, 2, 1, 1]
                        },
                        {
                            label: 'Calories Out',
                            backgroundColor: '#3f3f3f',
                            data: [2, 3, 4, 4]
                        }
                    ]
                },
                graph_style: {
                    position: 'relative',
                    height: '38vh'
                }
            }
        },
        methods: {
            getCalorieLog: function () {
                // Placeholder data
                this.datum = {
                    labels: ['2018-05-05', '2018-05-06', '2018-05-07', '2018-05-08'],
                    datasets: [
                        {
                            label: 'Calories In',
                            backgroundColor: '#f3f3f3',
                            data: [1, 2, 1, 1]
                        },
                        {
                            label: 'Calories Out',
                            backgroundColor: '#3f3f3f',
                            data: [2, 3, 4, 4]
                        }
                    ]
                }
            },
        }
    }
</script>
