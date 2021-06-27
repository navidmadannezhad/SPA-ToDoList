<template>
    <div class="drop-left " id="dropLeft">

        <div class="modal-nav">
            <div class="menu-button">
                <i class="fas fa-bars" @click="toggleMenu"></i>
            </div>
        </div>

            <div class="date-section">
            <div class="week-day">یکشنبه</div>
            <div class="date">
                <div class="day">
                    ۲۱
                </div>
                <div class="month">
                    شهریور
                </div>
                <div class="year">
                    ۱۳۷۸
                </div>
            </div>
        </div>

        <div class="menu">
            <a href="" @click="logout">خروج از پنل</a>
            <router-link to="/about">درباره سازنده</router-link>
        </div>

    </div>
</template>

<script>
export default {
    methods:{
        logout(){
            this.$store.dispatch('logout');
            this.$router.push('/');
        },

        toggleMenu(){
            this.$emit('toggleMenu');
        }
    }
}
</script>

<style lang="scss" scoped>
div.drop-left{
    position: absolute;
    top: 0px;
    right: 0px;
    width: 0px;
    overflow: hidden;
    height: 100%;
    background: #141E30; 
    background: -webkit-linear-gradient(to bottom right, #141E30, #243B55);
    background: linear-gradient(to bottom right, #141E30, #243B55);
    display: flex;
    flex-direction: column;
    align-items: center;
    transition: all 0.25s;
    div.modal-nav{
        font-size: 1.2rem;
        width: 100%;
        padding: 30px 30px 0px 0px;
    }
    div.date-section{
        padding: 30px 0px;
        margin-top: 50px;
        width: 80%;
        border-bottom: 2px solid rgba(255,255,255,0.1);
        opacity: 0.5;
        font-size: 1.2rem;
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        div.date{
            display: flex;
            & > div{
                padding-left: 10px;
            }
        }
    }
    div.menu{
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        width: 100%;
        min-width: 150px;
        padding: 30px;
        a{
            padding-bottom: 30px;
            text-decoration: none;
        }
    }
    }
</style>