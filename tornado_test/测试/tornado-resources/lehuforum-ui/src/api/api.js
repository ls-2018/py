import axios from 'axios'

let host = 'http://127.0.0.1:9001'

// 验证码
export const getVerifyCode = params => { return axios.post(`${host}/code/`, params) }

// 注册
export const registUser = params => { return axios.post(`${host}/register/`, params) }

// 登录
export const loginUser = params => { return axios.post(`${host}/login/`, params) }

// 获取小组列表
export const getCommunityGroups = params => { return axios.get(`${host}/groups/`, params) }

// 创建小组
export const createCommunityGroup = params => {
  return axios.post(`${host}/groups/`, params, { headers: { 'Content-Type': 'multipart/form-data' } })
}

// 申请加入小组
export const applyGroupMember = params => {
  return axios.post(`${host}/groups/${params.group_id}/members/`, { 'apply_reason': params.apply_reason })
}

// 获取小组详情
export const getSingleGroup = params => { return axios.get(`${host}/groups/${params.group_id}/`) }

// 发布帖子
export const createPost = params => {
  return axios.post(`${host}/groups/${params.group_id}/posts/`, { 'title': params.title, 'content': params.content })
}

// 获取指定小组的帖子列表
export const getPostList = params => {
  console.log(params)
  return axios.get(`${host}/groups/${params.params.group_id}/posts/`, params)
}

// 获取帖子详情
export const getPostDetail = params => { return axios.get(`${host}/posts/${params.post_id}/`) }

// 发布帖子评论
export const createPostComment = params => {
  return axios.post(`${host}/posts/${params.post_id}/comments/`, { 'content': params.content })
}

// 获取指定的帖子的评论列表
export const getPostComments = params => { return axios.get(`${host}/posts/${params.post_id}/comments/`) }

// 创建问题
export const createQuestion = params => {
  return axios.post(`${host}/questions/`, params, { headers: { 'Content-Type': 'multipart/form-data' } })
}

// 获取问题列表
export const getQuestionList = params => { return axios.get(`${host}/questions/`, params) }

// 获取问题详情
export const getQuestionDetail = params => { return axios.get(`${host}/questions/${params.question_id}/`) }

// 回答问题
export const createAnswer = params => {
  return axios.post(`${host}/questions/${params.question_id}/answers/`, { 'content': params.content })
}

// 获取指定的问题的回答列表
export const getAnswers = params => { return axios.get(`${host}/questions/${params.question_id}/answers/`) }

// 获取用户信息
export const getUserProfile = params => { return axios.get(`${host}/info/`, params) }

// 修改用户信息
export const changeUserProfile = params => { return axios.patch(`${host}/info/`, params) }

// 获取用户头像
export const getUserAvatar = params => { return axios.get(`${host}/avatar/`, params) }

// 提交用户头像
export const changeUserAvatar = params => { return axios.post(`${host}/avatar/`, params) }

// 提交密码表单
export const changeUserPassword = params => { return axios.post(`${host}/password/`, params) }

// 获取用户的消息列表
export const getUserMessages = params => { return axios.get(`${host}/messages/`, params) }

// 获取当前用户收到的所有小组的加入申请
export const getUserApplys = params => { return axios.get(`${host}/applys/`) }

// 处理收到的小组加入的申请
export const changeApplyStatus = params => {
  return axios.patch(`${host}/members/${params.apply_id}/`, { 'status': params.status, 'handle_msg': params.handle_msg })
}
