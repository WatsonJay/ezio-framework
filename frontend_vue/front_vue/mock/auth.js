module.exports = [
  {
    url: '/user/login',
    type: 'post',
    response: config => {
      return {
        code: 200,
        message: "登录成功",
        data: {
          userToken: '1234123441',
          userNickName: '@name',
          userPicUrl: 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
        }
      }
    }
  }
]