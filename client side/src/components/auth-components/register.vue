<template>
    <div class="register-comp">

        <message-component></message-component>

        <div class="content">
            <form action="">
                <input type="text" placeholder="نام کاربری..." v-model="username">
                <input type="password" placeholder="رمز عبور..." v-model="password">
                <input type="password" placeholder="تکرار رمز عبور..." v-model="password2">
                <button class="submit" @click="register($event)">ثبت نام</button>
            </form>
        </div>

    </div>
</template>

<script>
import messageComponent from '../message.vue';
import { msgLaunchMixin } from 'mixins';
export default {
    mixins: [
        msgLaunchMixin,
    ],
    components:{
        'message-component': messageComponent
    },
    data: function(){
        return{
            username: '',
            password: '',
            password2: '',
            messages: []
        }
    },

    methods:{
        register(event){
            event.preventDefault();
            let payload = {
                username: this.username,
                password: this.password,
                password2: this.password2
            };
            this.$store.dispatch('register', payload);
        }
    },

    watch:{
        messages(){
            this.launchMessageComponent(this.messages);
        }
    }
}
</script>


<style lang="scss" scoped>

@import '@/css/custom.scss';

div.register-comp{
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;

    div.content{
        width: 100%;
        form{
            display: flex;
            flex-direction: column;
            align-items: flex-end;
            & > *{
                margin-bottom: 30px;
            }
            input, button.submit{
                @include input();
            }
            button.submit{
                @include button();
            }
        }
    }
}
</style>