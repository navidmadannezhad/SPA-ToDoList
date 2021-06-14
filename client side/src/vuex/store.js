import Vuex from 'vuex'
import Vue from 'vue'
import axios from 'axios';
import { getCookie } from '../csrf';
import { router } from '../router/router';

Vue.use(Vuex);

export const store = new Vuex.Store({
    state:{
        tasks: [],
        serverMessagesBox: [],
        serverMessageState: false,
        /* User auth token */
        token: localStorage.getItem('token'),
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
                state.serverMessagesBox = messages;
                state.serverMessageState = false;
            })
        },

        login: function(state, args){
            axios({
                url: 'http://127.0.0.1:8000/api/login/',
                method: 'POST',
                data: args,
                headers:{
                    'X-CSRFToken': getCookie('csrftoken')
                }
                
            }).then(response => {
                let successMessage = {
                    'success': ['ورود با موفقیت انجام شد']
                }
                localStorage.setItem('user', response.data.user)
                localStorage.setItem('token', response.data.token);
                state.serverMessagesBox = successMessage;
                state.serverMessageState = true;

            }).catch(error => {
                let messages = error.response.data;
                state.serverMessagesBox = messages;
                state.serverMessageState = false;
            })
        },

        logout: function(){
            localStorage.removeItem('token');
            localStorage.removeItem('user');
        },



        getTasks: function(state){
            axios({
                url: 'http://127.0.0.1:8000/api/task-list/',
                method: 'GET',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken'),
                    'Authorization': `Token ${state.token}`
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
                    'X-CSRFToken': getCookie('csrftoken'),
                    'Authorization': `Token ${state.token}`
                },
                data: {
                    title: arg.title,
                    description: arg.description
                }
            }).then(response => {
                let tasks = state.tasks;
                state.tasks = [];
                // shows "no messages" and then the tasks
                setTimeout(()=>{
                    state.tasks = tasks;
                }, 1);
            }).catch(err => {
                console.log(err.response);
            })
        },

        deleteTask(state, arg){
            let title = arg.title;
            axios({
                url: `http://127.0.0.1:8000/api/task-delete/${title}/`,
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken'),
                    'Authorization': `Token ${state.token}`
                }
            }).then(response => {
                state.serverMessagesBox = response.data;
                state.serverMessageState = true;
            }).catch(err => {
                state.serverMessagesBox = err.response.data;
                state.serverMessageState = false;
            });
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

        deleteTask(context, payload){
            context.commit('deleteTask', payload);
        },

        register: function(context, payload){
            let args = {
                username: payload.username,
                password: payload.password,
                password2: payload.password2
            };
            context.commit('register', args);
        },

        login: function(context, payload){
            let args = {
                username: payload.username,
                password: payload.password
            }
            context.commit('login', args);
        },

        logout: function(context){
            context.commit('logout');
        },
    }
})