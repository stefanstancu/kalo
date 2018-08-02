<template>
    <div>
        <div class='ten columns'>
            <line_graph :chartData="datum"/>
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
                    <input type='number' placeholder='220' style='width:100%'></input>
                </div>
                <div class='two columns' style='padding-top:5px'>
                    <label>lbs</label>
                </div>
                <div class='four columns'>
                    <button class='button primary'>add weight</button>
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
    import line_graph from './graphs/line_graph.vue'
    import modal from './modal.vue'

    export default {
        props: [],
        components: {
            line_graph,
            modal
        },
        data: function () {
            return { 
                datum: { },
                showAddWeight: false
            }
        },
        methods: {
            getCalorieLog: function () {
                alert('send request for data');
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
            }
        }
    }
</script>
