import VueRouter from 'vue-router';
import Vue from 'vue';

import loginComponent from '../components/auth-components/login.vue';
import RegisterComponent from '../components/auth-components/register.vue';
import landingComponent from '../components/landing.vue';
import authComponent from '../components/auth-components/auth.vue';
import panelComponent from '../components/panel.vue'

Vue.use(VueRouter);

const routes = [
    {
        path: '/',
        component: landingComponent
    },

    {
        path: '/auth',
        component: authComponent,
        children: [
            {
                path: 'login',
                component: loginComponent
            },
            {
                path: 'register',
                component: RegisterComponent
            }
        ]
    },

    {
        path: '/panel',
        component: panelComponent
    },
]

export const router = new VueRouter({
    mode: 'history',
    routes
});