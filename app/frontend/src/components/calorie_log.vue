<template>
        <div>
            <div class='ten columns'>
                <line_graph ref="line_graph" :chartData="datum" :style="graph_style"/>
            </div>
            <div class='two columns'>
                <button class='button primary' @click='showAddCout=true'>+</button>
            </div>
            <modal v-if='showAddCout' @close='showAddCout=false' :size='{width: "50%", height: "20%"}'>
                <div slot='header'>
                    <h2>Log Calories Out</h2>
                </div>
                <div slot='body' class='row'>
                    <div class='three columns'>
                        <input type='number' placeholder='220' style='width:100%' v-model="cout.measure"></input>
                    </div>
                    <div class='one column' style='padding-top:5px'>
                        <label>Cal Out</label>
                    </div>
                    <div class='three columns'>
                        <input type='date' style='width:100%' v-model="cout.date"></input>
                    </div>
                    <div class='three columns'>
                        <button class='button primary' @click="sendCout">save</button>
                    </div>
                    <div class='two columns'>
                        <button class='button primary' @click="showAddCout=false">close</button>
                    </div>
                </div>
                <div slot='footer'></div>
            </modal>
        </div>
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
                            backgroundColor: 'rgba(83, 175, 204, 0.4)',
                            data: [1, 2, 1, 1]
                        },
                        {
                            label: 'Calories Out',
                            backgroundColor: 'rgba(207, 119, 75, 0.4)',
                            data: [2, 3, 4, 4]
                        }
                    ]
                },
                graph_style: {
                    position: 'relative',
                    height: '38vh'
                },
                showAddCout: false,
                cout: {
                    measure: 0,
                    date: 0
                }
            }
        },
        methods: {
            getCalorieLog: function () {
                axios.post('http://localhost:5000/api/getcalories', {}, {withCredentials: true}
                    ).then(response => {
                        console.log(response.data);
                        this.datum.labels = [];

                        this.datum.datasets[0].data =  [];
                        this.datum.datasets[1].data = [];

                        var dates = [];
                        for (var date in response.data.calories_in){
                            dates.push(date);
                        }
                        for (var date in response.data.calories_out){
                            if (!(date in dates)){
                                dates.push(date);
                            }
                        }
                        dates.sort();
                        this.datum.labels = dates;

                        for (var i in dates){
                            if (dates[i] in response.data.calories_in){
                                this.datum.datasets[0].data.push(response.data.calories_in[dates[i]]);
                            }
                            else {
                                this.datum.datasets[0].data.push(0);
                            }
                        }

                        for (var i in dates){
                            if (dates[i] in response.data.calories_out){
                                this.datum.datasets[1].data.push(response.data.calories_out[dates[i]]);
                            }
                            else {
                                this.datum.datasets[1].data.push(0);
                            }
                        }
                        
                        this.$refs.line_graph.render();
                    }).catch(error => {
                        console.log(error);
                    });
            },
            sendCout: function () {
                axios.post('http://localhost:5000/api/savecout', this.cout, {withCredentials: true}
                    ).then(response => {
                        if(response.status == 200){
                            this.showAddCout = !this.showAddCout;
                        }
                        this.getCalorieLog();
                        
                    }).catch(error => {
                        console.log(error);
                    });
            }
        }
    }
</script>
