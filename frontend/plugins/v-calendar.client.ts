import 'v-calendar/style.css'

import { Calendar, DatePicker, setupCalendar } from 'v-calendar'

export default defineNuxtPlugin((nuxtApp) => {
  nuxtApp.vueApp.use(setupCalendar, {})
  nuxtApp.vueApp.component('VCalendar', Calendar)
  nuxtApp.vueApp.component('VDatePicker', DatePicker)
})