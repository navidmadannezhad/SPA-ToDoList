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
                            <div class="edit">
                                <i class="fas fa-pencil-alt" @click="edit(task)"></i>
                            </div>
                            <div class="checkbox">
                                <i class="far fa-check-square" v-if="task.status" @click="changeTaskStatus(task.title)"></i>
                                <i class="far fa-square" @click="changeTaskStatus(task.title)" v-else></i>
                            </div>
                            <div class="trashcan">
                                <i class="fas fa-trash-alt" @click="deleteTask(task.title)"></i>
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

            <horizontal-menu v-on:toggleMenu="toggleMenu"></horizontal-menu>

        </div>

        <add-modal ref="addModal" id="addModal" :editableDescription="editableDescription" :editableTitle="editablTitle" :theNameOfTheTaskThatShouldBeUpdated="theNameOfTheTaskThatShouldBeUpdated"></add-modal>

    </div>
</template>

<script>
import addModal from './addModal.vue';
import msgComponent from './message.vue';
import horizontalMenu from './horizontalMenu.vue'

export default {
    data: function(){
        return{
            tasks: this.$store.state.tasks,
            addModalEditState: false,
            editablTitle: null,
            editableDescription: null,
            theNameOfTheTaskThatShouldBeUpdated: null
        }
    },
    components: {
        'add-modal': addModal,
        'message-component': msgComponent,
        'horizontal-menu': horizontalMenu
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
            let dropLeft = document.querySelector('#dropLeft');

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
                    setTimeout(()=>{
                        addModal.style.top = '180px';
                    },500);
                });
            }else{
                this.unBlurBackground().then(()=>{
                    setTimeout(()=>{
                        addModal.style.top = '200px';
                    },250);
                    setTimeout(()=>{
                        addModal.style.top = '-380px';
                    },500);
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
        },

        deleteTask(title){
            let payload = {
                title: title
            };
            if(confirm('واقعا میخوای این تسک رو پاک کنی؟')){
                this.$store.dispatch('deleteTask', payload);
            }
        },

        changeTaskStatus(title){
            let payload = {
                title: title
            }
            this.$store.dispatch('changeTaskStatus', payload);
        },

        edit(task){
            this.setAddModalForEdit(task);
        },

        setAddModalForEdit(task){
            this.injectTaskDataIntoAddModal(task);
            this.toggleAddModal();
        },

        injectTaskDataIntoAddModal(task){
            this.theNameOfTheTaskThatShouldBeUpdated = task.title;
            this.editablTitle = task.title;
            this.editableDescription = task.description;
        },

        emptyAddModalFromProp(){
            this.theNameOfTheTaskThatShouldBeUpdated = null;
            this.editablTitle = null;
            this.editableDescription = null;
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
            let dropLeft =  document.querySelector('#dropLeft');
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
                        width:40%;
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

    }
}

</style>