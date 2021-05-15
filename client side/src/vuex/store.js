import Vuex from 'vuex'
import Vue from 'vue'
import axios from 'axios';

Vue.use(Vuex);

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

export const store = new Vuex.Store({
    state:{
        numb: 1
    },
    mutations:{
        addTask: function(){
            axios({
                url: 'http://127.0.0.1:8000/api/task-list/',
                method: 'GET',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken')
                }
            }).then(response => {
                console.log(response.data);
            }).catch(err => {
                console.log(err.response);
            })
        }
    },
    actions:{

    }
})