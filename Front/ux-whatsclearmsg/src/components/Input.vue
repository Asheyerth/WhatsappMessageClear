<template>
<h2>
    Ingresar mensaje
</h2>
<form>
    <input type="text" v-model="userInput">
    {{ userInput }}
</form>
<button v-on:click=clearMessage>Limpiar</button>

</template>


<script>
export default {
  name: 'InputMessage',
  methods: {
    clearMessage(){
        //Envio a backend
        //axios
    }
  },
  data(){
    return {
        userInput: ""
    }
  }
  //props: {
    //msg: String
  //}
}
</script>