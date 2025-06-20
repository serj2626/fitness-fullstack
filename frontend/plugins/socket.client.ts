// import { io } from 'socket.io-client';

// export default defineNuxtPlugin(() => {
//   const socket = io('http://localhost:8000', {
//     transports: ['websocket'],
//   });

//   return {
//     provide: {
//       socket,
//     },
//   };
// });

// const { $socket } = useNuxtApp();

// onMounted(() => {
//   $socket.on('chat_message', (msg) => {
//     console.log('Сообщение:', msg);
//   });
// });

// function sendMessage(text: string) {
//   $socket.emit('chat_message', text);
// }


// #############################


// <template>
//   <div>
//     <div v-for="msg in messages" :key="msg">{{ msg }}</div>
//     <input v-model="text" @keyup.enter="send" />
//   </div>
// </template>

// <script setup>
// const { $socket } = useNuxtApp();
// const messages = ref<string[]>([]);
// const text = ref('');

// onMounted(() => {
//   $socket.on('chat_message', (msg) => {
//     messages.value.push(msg);
//   });
// });

// function send() {
//   if (text.value.trim()) {
//     $socket.emit('chat_message', text.value);
//     text.value = '';
//   }
// }
// </script>