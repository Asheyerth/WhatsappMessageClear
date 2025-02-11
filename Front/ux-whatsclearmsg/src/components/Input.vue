<template>
<h2>
    Ingresar mensaje
</h2>
<Textarea v-model="userInput.message" placeholder="Ingrese su mensaje"></Textarea>
<form>
    <input type="text" v-model="userInput.name">
    <input type="text" v-model="userInput.age">
    <button v-on:click=clearMessage>Limpiar</button>
</form>
{{ userInput }}
{{ userInput.message }}

</template>

<script>
//<input type="text" v-model="userInput.message">
//import axios from 'axios';
//import api from './plugins/axios.js';
export default {
  name: 'PostRequestClearMessage',
  data(){
    return {
      userInput: {
        message: 'mensaje',
        name: 'nombre',
        age: 'edad'
      }
    }
  },
  methods: {
    async clearMessage() {
      try {
        console.log('Enviando')
        const response = await this.$axios.post('/procesarMensaje', {
          // Datos que deseas enviar
          input: this.userInput
        });
        console.log('Enviado y revisado')
        console.log(response.data); // La respuesta del servidor
      } catch (error) {
        console.error('Error al enviar la solicitud:', error);
      }
    }//,
    //Otro endpoint 
    //async deleteMessage() {asdasdas}
  }
}




//export default {
//  name: 'InputMessage',
//  methods: {
//    clearMessage(){
        //Envio a backend
        //axios

//    }
//  },
//  data(){
//    return {
//        userInput: ""
//    }
//  }
  //props: {
    //msg: String
  //}
//}
</script>