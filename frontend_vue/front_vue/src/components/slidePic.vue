<template>
  <div class="slider_validate">
    <div class="slider_pic">
      <canvas id="back_img"></canvas>
      <canvas id="slider_block"></canvas>
    </div>
    <div class="sliding_bar">
      <div class="sliding_bg" :class="{ puzzleTrue: puzzle }">
        {{ tips }}
      </div>
      <div
        class="sliding_btn icon-tech icon-liebiao"
        @mousedown.prevent="drag"
      ></div>
    </div>
    <div class="sliding-option"></div>
  </div>
</template>

<script>
export default {
  name: "slidePic",
  data() {
    return {
      //滑块x轴数据
      tips: this.$t("tip.slidingPic"),
      slider: {
        mx: 0,
        bx: 0
      },
      //拼图是否正确
      puzzle: false
    };
  },
  props: {},
  mounted() {
    this.sliderInit();
  },
  methods: {
    //拼图验证码初始化
    sliderInit() {
      //生成指定区间的随机数
      const random = (min, max) => {
        return Math.floor(Math.random() * (max - min + 1) + min);
      };
      //x: 254, y: 109
      let mx = random(130, 244),
        bx = random(10, 120),
        y = random(10, 99);

      this.slider = { mx, bx };
      this.draw(mx, bx, y);
    },
    draw(mx = 200, bx = 20, y = 50) {
      var backDom = document.querySelector("#back_img");
      var backImg = backDom.getContext("2d");

      let blockDom = document.querySelector("#slider_block");
      let block = blockDom.getContext("2d");

      var img = new Image();
      img.src = "https://picsum.photos/300/160";
      backDom.height = img.height;
      blockDom.height = img.height;
      let mainxy = { x: mx, y: y, r: 9 };
      let blockxy = { x: bx, y: y, r: 9 };
      this.drawBlock(backImg, mainxy, "fill");
      this.drawBlock(block, blockxy, "clip");
      img.onload = function() {
        backImg.drawImage(img, 0, 0, img.width, img.height);
        block.drawImage(img, bx - mx, 0, img.width, img.height);
      };
    },
    drawBlock(dom, pos = { x: 254, y: 109, r: 9 }, type) {
      let x = pos.x,
        y = pos.y,
        r = pos.r,
        w = 30;
      let PI = Math.PI;
      //绘制
      dom.beginPath();
      //left
      dom.moveTo(x, y);
      //top
      dom.arc(x + (w + 5) / 2, y, r, -PI, 0, true);
      dom.lineTo(x + w + 5, y);
      //right
      dom.arc(x + w + 5, y + w / 2, r, 1.5 * PI, 0.5 * PI, false);
      dom.lineTo(x + w + 5, y + w);
      //bottom
      dom.arc(x + (w + 5) / 2, y + w, r, 0, PI, false);
      dom.lineTo(x, y + w);
      dom.arc(x, y + w / 2, r, 0.5 * PI, 1.5 * PI, true);
      dom.lineTo(x, y);
      //修饰，没有会看不出效果
      dom.lineWidth = 2;
      dom.fillStyle = "rgba(255, 255, 255, 0.5)";
      dom.strokeStyle = "rgba(255, 255, 255, 0.8)";
      dom.stroke();
      dom[type]();
      dom.globalCompositeOperation = "xor";
    },
    //鼠标按下
    drag(e) {
      let dom = e.target; //dom元素
      let slider = document.querySelector("#slider_block"); //滑块dom
      const downCoordinate = { x: e.x, y: e.y };

      //正确的滑块数据
      let checkx = Number(this.slider.mx) - Number(this.slider.bx);
      //x轴数据
      let x = 0;
      const move = moveEV => {
        x = moveEV.x - downCoordinate.x;
        if (x >= 251 || x <= 0) return false;
        dom.style.left = x + "px";
        slider.style.left = x + "px";
      };

      const up = () => {
        document.removeEventListener("mousemove", move);
        document.removeEventListener("mouseup", up);
        dom.style.left = "";
        let max = checkx + 2;
        let min = checkx - 2;
        //允许正负误差1
        if ((max >= x && x >= min) || x === checkx) {
          this.puzzle = true;
          this.tips = this.$t("tip.slidingPicSuccess");
          this.$emit("verify");
        } else {
          this.tips = this.$t("tip.slidingPicError");
          this.puzzle = false;
          this.sliderInit();
        }
      };

      document.addEventListener("mousemove", move);
      document.addEventListener("mouseup", up);
    }
  }
};
</script>

<style lang="scss" scoped>
.slider_validate {
  .slider_pic {
    position: relative;
    width: 100%;
    height: 160px;
    #back_img,
    #slider_block {
      position: absolute;
      left: 0;
      top: 0;
      //width: inherit;
      height: inherit;
    }
    #slider_block {
      z-index: 4000;
    }
  }
  .sliding_bar {
    width: 100%;
    height: 50px;
    border-bottom: #c7c9d0 1px solid;
    display: flex;
    align-items: center;
    justify-content: flex-start;
    .sliding_bg {
      margin-left: 7px;
      width: 286px;
      height: 28px;
      background: rgba(28, 136, 188, 0.5);
      border-radius: 25px;
      font-size: 14px;
      line-height: 28px;
      padding-right: 15px;
      padding-left: 70px;
    }
    .puzzleTrue {
      background: #67c23a;
      color: #ffffff;
    }
    .sliding_btn {
      position: absolute;
      width: 40px;
      height: 40px;
      line-height: 42px;
      background: #ffffff;
      box-shadow: #b9bdc8 0 0 3px;
      border-radius: 50%;
      left: 7px;
      text-align: center;
      font-size: 28px;
      color: #3e5d8b;
      &:hover {
        color: #2181bd;
      }
    }
  }
}
</style>
