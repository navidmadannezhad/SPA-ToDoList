import Vuex from 'vuex'
import Vue from 'vue'
import axios from 'axios';
import { getCookie } from '../csrf';
import { router } from '../router/router';

Vue.use(Vuex);

export const store = new Vuex.Store({
    state:{
        tasks: [],
        messages: [],
        /* User auth token */
        token: ''
    },
    mutations:{
        /* Authentication methods */
        register: function(state, args){
            axios({
                url: 'http://127.0.0.1:8000/api/register/',
                data: {
                    username: args.username,
                    password: args.password,
                    password2: args.password2
                },
                headers: {
                    'X-CSRFToken': getCookie('csrftoken')
                },
                method: 'POST'
            }).then(response => {
                window.localStorage.setItem('token', response.data);
                setTimeout(()=>{
                    router.push({name: 'panel'});
                },2000);
            }).catch(error => {
                let messages = error.response.data;

                Object.keys(messages).forEach(key => {
                    let message = {};
                    message.content = messages[key][0];
                    message.success = false;
                    state.messages.push(object);
                })
                //console.log(error.response.data);
            })
        },

        login: function(){

        },

        logout: function(){

        },



        getTasks: function(state){
            axios({
                url: 'http://127.0.0.1:8000/api/task-list/',
                method: 'GET',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken')
                }
            }).then(response => {
                state.tasks = response.data;
                console.log(response.data);
            }).catch(err => {
                console.log(err.response);
            })
        },

        createTask: function(state, arg){
            axios({
                url: 'http://127.0.0.1:8000/api/task-create/',
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken')
                },
                data: {
                    title: arg.title,
                    description: arg.description
                }
            }).then(response => {
                state.tasks = response.data;
                console.log(response.data);
            }).catch(err => {
                console.log(err.response);
            })
        },

        serverMessageOrganizer(state){

        }
    },
    actions:{
        getTasks: function(context){
            context.commit('getTasks');
        },

        createTask: function(context, payload){
            let args = {
                title: payload.title,
                description: payload.description
            }
            context.commit('createTask', args);
        },

        register: function(context, payload){
            let args = {
                username: payload.username,
                password: payload.password,
                password2: payload.password2
            };
            context.commit('register', args);
        },

        login: function(context){
            context.commit('login');
        },

        logout: function(context){
            context.commit('logout');
        },

        serverMessageOrganizer(context,){
            context.commit('serverMessageOrganizer');
        }
    }
})