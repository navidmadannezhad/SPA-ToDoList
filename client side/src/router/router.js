import VueRouter from 'vue-router';
import Vue from 'vue';

import loginComponent from '../components/auth-components/login.vue';
import RegisterComponent from '../components/auth-components/register.vue';
import landingComponent from '../components/landing.vue';
import authComponent from '../components/auth-components/auth.vue';
import panelComponent from '../components/panel.vue'
import axios from 'axios';
import { getCookie } from '../csrf';

Vue.use(VueRouter);

const routes = [
    {
        path: '/',
        name: 'home',
        component: landingComponent
    },

    {
        path: '/auth',
        component: authComponent,
        children: [
            {
                path: 'login',
                name: 'login',
                component: loginComponent
            },
            {
                path: 'register',
                name: 'register',
                component: RegisterComponent
            }
        ]
    },

    {
        path: '/panel',
        name: 'panel',
        component: panelComponent
    },
]

export const router = new VueRouter({
    mode: 'history',
    routes
});

/* Authentication manager -- */
// router.beforeEach((from, to, next) => {
//     let nextIsPanel = to.name == 'panel';

//     if(nextIsPanel){
//         if(isAuthenticated()){
//             next();
//             console.log('apmoce');
//         }else{
//             router.push({name: 'login'});
//             console.log('no');
//         }
//     }
//     // next();
//     // let token = localStorage.getItem('token');
//     // tokenIsValid('72ff590fc9285f800ebb3c9aae5543f00214807e');
// });

// function isAuthenticated(){
//     let token = window.localStorage.getItem('token');

//     if(token && tokenIsValid(token)){
//         return true;
//     }else{
//         return false;
//     }
// }

// function tokenIsValid(token){
//     axios({
//         url: 'http://127.0.0.1:8000/api/authenticate-token/',
//         data: {
//             'token': token
//         },
//         headers:{
//             'X-CSRFToken': getCookie('csrftoken')
//         },
//         method: 'POST'
//     }).then(response => {
//         return true;
//     }).catch(err => {
//         return false;
//     })
// }
