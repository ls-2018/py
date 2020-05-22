import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/regist',
      name: 'regist',
      component: () => import('./views/Register.vue')
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('./views/Login.vue')
    },
    {
      path: '/user/info',
      name: 'user_info',
      component: () => import('./views/UserInfo.vue')
    },
    {
      path: '/user/center/',
      name: 'user_center',
      component: () => import('./views/UserCenter.vue'),
      children: [
        {
          path: 'groups',
          name: 'my_groups',
          component: () => import('./views/MyGroups.vue')
        },
        {
          path: 'postcomments',
          name: 'my_postcomments',
          component: () => import('./views/MyPostComments.vue')
        },
        {
          path: 'questions',
          name: 'my_questions',
          component: () => import('./views/MyQuestions.vue')
        },
        {
          path: 'answers',
          name: 'my_answers',
          component: () => import('./views/MyAnswers.vue')
        },
        {
          path: 'applys',
          name: 'my_applys',
          component: () => import('./views/MyApplys.vue')
        }
      ]
    },
    {
      path: '/groups',
      name: 'groups',
      component: () => import('./views/GroupList.vue')
    },
    {
      path: '/group/create',
      name: 'group_create',
      component: () => import('./views/GroupCreate.vue')
    },
    {
      path: '/groups/:id/',
      name: 'group_detail',
      component: () => import('./views/GroupDetail.vue'),
      children: [
        {
          path: 'post/create',
          name: 'post_create',
          component: () => import('./views/PostCreate.vue')
        },
        {
          path: 'post/list',
          name: 'post_list',
          component: () => import('./views/PostList.vue')
        },
        {
          path: 'post/:pid/detail',
          name: 'post_detail',
          component: () => import('./views/PostDetail.vue')
        }
      ]
    },
    {
      path: '/questions',
      name: 'question_list',
      component: () => import('./views/QuestionList.vue')
    },
    {
      path: '/question/create',
      name: 'question_create',
      component: () => import('./views/QuestionCreate.vue')
    },
    {
      path: '/questions/:id/',
      name: 'question_detail',
      component: () => import('./views/QuestionDetail.vue')
    }
  ]
})
