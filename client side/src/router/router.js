import VueRouter from 'vue-router';
import Vue from 'vue';

import loginComponent from '../components/auth-components/login.vue';
import RegisterComponent from '../components/auth-components/register.vue';
import landingComponent from '../components/landing.vue';
import authComponent from '../components/auth-components/auth.vue';
import notFoundComponent from '../components/notFound.vue'
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
        component: panelComponent,
        beforeEnter: (from, to, next) => {
            let token = localStorage.getItem('token');
            if(token){
                tokenIsValid(token).then(response => {
                    next();
                }).catch(err => {
                    next({name: 'login'});
                })
            }else{
                next({name: 'login'});
            }
        }
    },
    {
        path: '*',
        name: 'notFound',
        component: notFoundComponent
    }
]

const router = new VueRouter({
    mode: 'history',
    routes
});



function tokenIsValid(token){
    return axios({
        url: 'http://127.0.0.1:8000/api/authenticate-token/',
        data: {
            'token': token
        },
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken')
        }
    });
}


export { router };