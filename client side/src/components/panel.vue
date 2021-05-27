<template>
    <div class="panel-comp" ref="panelComp">
        
        <message-component></message-component>

        <div class="content">
            <nav ref="nav">
                <div class="menu-button">
                    <i class="fas fa-bars" @click="toggleMenu"></i>
                </div>
                <div class="user-info">
                    <span>سلام</span>
                    <span> navid.mnzh!</span>
                </div>
                <div class="spacer"></div>
            </nav>

            <div class="tasks no-tasks" ref="tasks" v-if="!tasks.length">
                برای امروز برنامه ای نداری؟ حداقل یدونه اضافه کن!
            </div>
            <div class="tasks" ref="tasks" v-else>

                <div ref="task1" class="task" @click="toggleTask($event)" v-for="task in tasks" v-bind:key="task.id">
                    <div class="task-header">
                        <div class="task-title">{{ task.title }}</div>
                        <div class="buttons">
                            <div class="checkbox">
                                <i class="far fa-check-square" v-if="task.status"></i>
                                <i class="far fa-square" v-else></i>
                            </div>
                            <div class="trashcan">
                                <i class="fas fa-trash-alt"></i>
                            </div>
                        </div>
                    </div>
                    <div class="task-body">
                            {{ task.description }}
                    </div>
                </div>


            </div>

            <div class="add-button" ref="addButton">
                <button @click="toggleAddModal">
                    <i class="fas fa-plus"></i>
                </button>
            </div>



            <div class="drop-left" ref="dropLeft">

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
                    <router-link to="/">خروج از پنل</router-link>
                    <router-link to="/about">درباره سازنده</router-link>
                </div>

            </div>



        </div>

        <add-modal ref="addModal" id="addModal"></add-modal>

    </div>
</template>

<script>
import addModal from './addModal.vue';
import msgComponent from './message.vue';

export default {
    data: function(){
        return{
            tasks: this.$store.state.tasks
        }
    },
    components: {
        'add-modal': addModal,
        'message-component': msgComponent
    },
    methods:{
        toggleTask: function(event){
            let elementHasClassTaskHeaderOrTaskTitle = event.target.classList.contains('task-title');
            if(elementHasClassTaskHeaderOrTaskTitle){
                let taskBody = event.target.parentElement.nextElementSibling;
                if(taskBody.style.maxHeight){
                    taskBody.style.maxHeight = null;
                    taskBody.style.marginTop = '0px';
                }else{
                    taskBody.style.maxHeight = taskBody.scrollHeight + 'px';
                    taskBody.style.marginTop = '20px';
                }
            }
        },

        toggleMenu: function(){
            let tasks = this.$refs.tasks;
            let backgroundIsNotBlurred = tasks.style.filter != 'blur(2px)';
            let dropLeft = this.$refs.dropLeft;

            if(backgroundIsNotBlurred){
                this.blurBackground().then(()=>{
                    setTimeout(()=>{
                        dropLeft.style.width = '50%';
                    },250);
                });
            }else{
                this.unBlurBackground().then(()=>{
                    setTimeout(()=>{
                        dropLeft.style.width = '0px';
                    },250);
                });
            }
        },

        toggleAddModal: function(){
            let addModal = document.querySelector('#addModal');
            let tasks = this.$refs.tasks;
            let backgroundIsNotBlurred = tasks.style.filter != 'blur(2px)';

            if(backgroundIsNotBlurred){
                this.blurBackground().then(()=>{
                    setTimeout(()=>{
                        addModal.style.top = '200px';
                    },250);
                });
            }else{
                this.unBlurBackground().then(()=>{
                    setTimeout(()=>{
                        addModal.style.top = '-380px';
                    },250);
                });
            }
        },

        blurBackground: function(){
            let pro = new Promise((resolve, reject) => {
                let tasks = this.$refs.tasks;
                let nav = this.$refs.nav;
                let addButton = this.$refs.addButton;

                let fadingElements =  [tasks, nav, addButton];
                fadingElements.forEach(element => {
                    element.style.filter = 'blur(2px)';
                });
                resolve();
            });
            return pro;
        },

        unBlurBackground: function(){
            let pro = new Promise((resolve, reject) => {
                let tasks = this.$refs.tasks;
                let nav = this.$refs.nav;
                let addButton = this.$refs.addButton;

                let fadingElements =  [tasks, nav, addButton];
                fadingElements.forEach(element => {
                    element.style.filter = 'blur(0px)';
                });
                resolve();
            });
            return pro;
        },

        getTasks: function(){
            this.$store.dispatch('getTasks');
        }
    },

    computed:{
        storeTasks: function(){
            return this.$store.state.tasks;
        }
    },

    watch:{
        storeTasks(){
            this.tasks = this.storeTasks;
            console.log('changed');
        }
    },

    mounted(){
        this.getTasks();

        // close the left menu when the user clicks on any where except the menu
        window.addEventListener('click', (event) => {
            console.log(event.target.parentNode);
            let dropLeft = this.$refs.dropLeft;
            let dropLeftIsOpen = dropLeft.style.width == '50%';
            let elementClasses = event.target.classList;
            let elementParentClasses = event.target.parentNode.classList;

            if(dropLeftIsOpen){
                    if(elementClasses.contains('drop-left') || elementParentClasses.contains('date') || elementParentClasses.contains('date-section') || elementParentClasses.contains('menu')){
                    console.log('nothing!');
                }else{
                    this.unBlurBackground().then(()=>{
                        setTimeout(()=>{
                            dropLeft.style.width = '0px';
                        },250);
                    });
                }
            }


        });
    }
}
</script>

<style lang="scss" scoped>
div.panel-comp{
    width: 100%;
    min-height: 100vh;
    background: #141E30; 
    background: -webkit-linear-gradient(to left, #243B55, #141E30);
    background: linear-gradient(to left, #243B55, #141E30);
    display: flex;
    flex-direction: column;
    align-items: center;
    font-family: iransansweb;
    div.content{
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        nav{
            display: flex;
            justify-content: space-between;
            align-items: center;
            width: 100%;
            transition: all 0.25s;
            & > *{
                padding: 30px;
                font-size: 1.2rem;
            }
        }
        div.no-tasks{
            color: #45b884;
            font-weight: bold;
            font-size: 1.2rem;
        }
        div.tasks{
            margin-top: 80px;
            width: 80%;
            display: flex;
            flex-direction: column;
            align-items: center;
            transition: all 0.25s;
            margin-bottom: 100px;
            div.task{
                margin-top: 20px;
                width: 330px;
                background-color: #45b884;
                border-radius: 15px;
                display: flex;
                flex-direction: column;
                padding: 20px;
                & > div{
                    width: 100%;
                }
                div.task-header{
                    display: flex;
                    justify-content: space-between;
                    div.task-title{
                        width: 80%;
                    }
                    div.buttons{
                        width: 20%;
                        display: flex;
                        justify-content: space-between;
                        font-size: 1.2rem;
                        div.trashcan i{
                            color: #ff2e2e;
                        }
                    }
                }
                div.task-body{
                    max-height: 0px;
                    height: 100%;
                    word-wrap: break-word;
                    overflow: hidden;
                    transition: all 0.25s;
                }
            }
        }

        div.add-button{
            position: fixed;
            width: 100%;
            bottom:30px;
            text-align: center;
            transition: all 0.25s;
            button{
                padding: 20px 25px;
                border: none;
                border-radius: 50%;
                color: white;
                font-size: 2.2rem;
                background-color: #45b884;
                box-shadow: 0px 4px 4px rgba(0,0,0,0.25), 0px 0px 100px black;
                i{
                    display: flex;
                }
            }
        }

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

    }
}

</style>