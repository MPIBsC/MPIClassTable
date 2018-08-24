import Vue from 'vue'
import Router from 'vue-router'
import QueryCht from '@/components/QueryCht.vue'
import QueryEn from '@/components/QueryEn.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'QueryEn',
      component: QueryEn
    },
    {
      path: '/en',
      name: 'QueryEn',
      component: QueryEn
    },
    {
      path: '/zh_hant',
      name: 'QueryCht',
      component: QueryCht
    }
  ]
})
