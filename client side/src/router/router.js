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
router.beforeEach((to, from, next)=>{
    let nextIsPanel = to.name == 'panel';

    if(nextIsPanel){
        if(isAuthenticated()){
            next();
        }else{
            next({name: 'login'});
        }
    }else{
        next();
    }
});

function isAuthenticated(){
    let token = window.localStorage.getItem('token');

    if(token && tokenIsValid(token)){
        return true;
    }else{
        return false;
    }
}

function tokenIsValid(token){
    axios({
        url: 'http://127.0.0.1:8000/api/authenticate-token/',
        method: 'POST',
        data:{
            token: token
        },
        headers:{
            'X-CSRFToken': getCookie('csrftoken')
        }
    }).then(response => {
        window.localStorage.setItem(user, response.data);
        return true;
    }).catch(err => {
        return false;
    })
}