<template>
    <div class="login-comp">

        <message-component :serverMessagesBox="serverMessagesBox" :serverMessageState="serverMessageState"></message-component>

        <div class="content">
            <form action="">
                <input type="text" placeholder="نام کاربری..." v-model="username">
                <input type="password" placeholder="رمز عبور..." v-model="password">
                <button class="submit" @click="login($event)">ورود</button>
            </form>
        </div>

    </div>
</template>

<script>
import messageComponent from '../message.vue';
export default {
    components:{
        'message-component': messageComponent
    },

    data(){
        return{
            username: '',
            password: ''
        }
    },

    methods:{
        login(event){
            event.preventDefault();
            
            let payload = {
                username: this.username,
                password: this.password
            };
            this.$store.dispatch('login', payload)
        }
    },

    computed:{
        serverMessagesBox(){
            return this.$store.state.serverMessagesBox;
        },

        serverMessageState(){
            return this.$store.state.serverMessageState;
        }
    }
}
</script>


<style lang="scss" scoped>

@import '@/css/custom.scss';

div.login-comp{
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