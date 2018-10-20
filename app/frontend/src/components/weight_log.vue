<template>
        <div>
            <div class='ten columns'>
                <line_graph ref="line_graph" :chartData="datum" :style="graph_style" />
            </div>
            <div class='two columns'>
                <button class='button primary' @click='showAddWeight=true'>+</button>
            </div>
            <modal v-if='showAddWeight' @close='showAddWeight=false' :size='{width: "50%", height: "20%"}'>
                <div slot='header'>
                    <h2>Log Weight</h2>
                </div>
                <div slot='body' class='row'>
                    <div class='three columns'>
                        <input type='number' placeholder='220' style='width:100%' v-model="weight.measure"></input>
                    </div>
                    <div class='two columns' style='padding-top:5px'>
                        <label>lbs</label>
                    </div>
                    <div class='four columns'>
                        <button class='button primary' @click="sendWeight">add weight</button>
                    </div>
                    <div class='three columns'>
                        <button class='button primary' @click="showAddWeight=false">close</button>
                    </div>
                </div>
                <div slot='footer'></div>
            </modal>
        </div>
</template>

<script>
    import axios from 'axios'
    import modal from './modal.vue'
    import line_graph from './graphs/line_graph.vue'

    export default {
        props: [],
        components: {
            line_graph,
            modal
        },
        data: function () {
            return { 
                datum: {
                    labels: ['2018-05-05', '2018-05-06', '2018-05-07'],
                    datasets: [
                        {
                            label: 'Weight',
                            backgroundColor: '#f3f3f3',
                            data: [1, 2, 1]
                        }
                    ]
                },
                graph_style: { 
                    position: 'relative',
                    height: '35vh',
                    width: '100%'
                },
                showAddWeight: false,
                weight: {
                    measure: 220,
                    unit: "lbs"
                }
            }
        },
        methods: {
            getWeightLog: function () {
                axios.post('http://localhost:5000/api/getweight', {}, {withCredentials: true}
                    ).then(response => {
                        this.datum.labels = [];
                        this.datum.datasets[0].data = [];
                        for (var i in response.data){
                            this.datum.labels.push(response.data[i].date);
                            this.datum.datasets[0].data.push(response.data[i].lbs);
                        }
                        this.$refs.line_graph.render();
                    }).catch(error => {
                        console.log(error);
                    });
            },
            sendWeight: function () {
                console.log(this.weight);
                axios.post('http://localhost:5000/api/saveweight', this.weight, {withCredentials: true}
                ).then(response => {
                    this.showAddWeight = false;
                    this.getWeightLog();
                }).catch(error => {
                    console.log(error);
                });
            }
        }
    }
</script>
