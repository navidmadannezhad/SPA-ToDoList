<template>
    <div class="modal-comp">

        <div class="form task-create-mode" v-if="!addModalIsEditModal">
            <input type="text" placeholder="نام برنامه..." ref="titleInput" v-model="title" v-on:input="checkTitleLength">
            <p class="validate-length">20/{{ title.length }}</p>
            <textarea placeholder="توضیحات..." v-model="description" v-on:input="checkDescLength" ref="description"></textarea>
            <p class="validate-length">120/{{ description.length }}</p>

            <button id="submit-plan" @click="createTask">ثبت برنامه</button>
        </div>

        <div class="form task-create-mode" v-else>
            <input type="text" placeholder="نام برنامه..." ref="titleInput" v-model="editableTitle" v-on:input="checkTitleLength">
            <p class="validate-length">20/{{ title.length }}</p>
            <textarea placeholder="توضیحات..." v-model="editableDescription" v-on:input="checkDescLength" ref="description"></textarea>
            <p class="validate-length">120/{{ description.length }}</p>

            <button id="submit-plan" @click="updateTask">بروزرسانی</button>
        </div>

        <div class="loading">

        </div>

    </div>
</template>


<script>
export default {
    props: [
        'editableTitle',
        'editableDescription',
        'theNameOfTheTaskThatShouldBeUpdated'
    ],
    data: function(){
        return{
            title: '', 
            description: '',
        }
    },
    methods: {
        checkTitleLength: function(){
            if(this.title.length > 20){
                this.title = this.title.substring(0,20);
            }
        },

        checkDescLength: function(){
            if(this.description.length > 120){
                this.description = this.description.substring(0,120);
            }
        },

        createTask: function(){
            this.$store.dispatch('createTask', {title: this.title, description: this.description});
            this.$parent.toggleAddModal();
        },

        updateTask(){
            let data = {
                title: this.editableTitle,
                description: this.editableDescription, theNameOfTheTaskThatShouldBeUpdated: this.theNameOfTheTaskThatShouldBeUpdated
            }
            this.$store.dispatch('updateTask', data);
            this.$parent.toggleAddModal();
            this.$parent.emptyAddModalFromProp();
        }
    },

    computed:{
        addModalIsEditModal(){
            if(this.editableTitle && this.editableDescription && this.theNameOfTheTaskThatShouldBeUpdated){
                return true;
            }else{
                return false;
            }
        },
    },

    mounted(){
        // close the add modal when the user clicks on any where except the add modal
        window.addEventListener('click', (event) => {
            
            let addModal = document.querySelector('#addModal');
            let addModalIsOpen = addModal.style.top == '200px';
            let elementClasses = event.target.classList;
            let elementName = event.target.tagName;
            let elementParentClasses = event.target.parentNode.classList;
            
            if(addModalIsOpen){
                if(elementClasses.contains('modal-comp') || elementParentClasses.contains('form')){
                    console.log('nothing!');
                }else{
                     this.$parent.unBlurBackground().then(()=>{
                         setTimeout(()=>{
                            addModal.style.top = '200px';
                        },250);
                        setTimeout(()=>{
                            addModal.style.top = '-380px';
                            this.$parent.emptyAddModalFromProp();
                        },500);
                    });
                }                
            }


        });
    }
}
</script>


<style lang="scss" scoped>
div.modal-comp{
    background: #141E30; 
    background: -webkit-linear-gradient(to left, #243B55, #141E30);
    background: linear-gradient(to left, #243B55, #141E30);

    position: absolute;
    top: -380px;
    
    padding: 30px 50px;
    border-radius: 20px;

    transition: all 0.25s;
    
    div.form{
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;

        & > *:not(button){
            width: 90%;
            padding: 10px;
            border: none;
            border-radius: 10px;
        }

        input, input::placeholder, input:focus, textarea, textarea::placeholder, textarea:focus{
            color: black !important;
            font-size: 1rem;
            outline: none;
        }

        p.validate-length{
            font-size: 0.8rem;
            margin: 5px 0px 5px 0px;
        }

        textarea{
            height: 110px;
        }

        button{
            background-color: #45b884;
            padding: 15px 50px;
            border: none;
            border-radius: 50px;
        }
    }
}
</style>