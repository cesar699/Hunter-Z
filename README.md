<!-- Hunter-Z | Anti-Fraud APK Analyzer -->
<h1 align="center">Hunter-Z 🔎🛡️</h1>
<p align="center">
  <em>以「反诈」为使命的 APK 接口分析平台</em><br>
  一键完成 <strong>行为路径解析 · 动态沙箱监控 · 弱口令爆破 · 权限风险评估</strong>
</p>
<p align="center">
  <img src="https://img.shields.io/badge/release-v1.3--beta-blue">
  <img src="https://img.shields.io/docker/pulls/hunterz/hunter-z?logo=docker">
  <img src="https://img.shields.io/github/actions/workflow/status/yourname/hunter-z/docker.yml?label=CI">
</p>

---

## ✨ 功能总览

| 模块 | 说明 |
| ---- | ---- |
| **静态接口解包** | apktool + jadx，抽取 URL / IP / API 路径 |
| **权限风险评分** | 自定义矩阵，前端可视化编辑 | 
| **动态沙箱监控** | gVisor + docker-android，60 s 实机运行，抓 tcpdump＋Frida Hook，生成流量折线图 |
| **批量上传 & 任务队列** | 拖拽多选、一键上传；SSE 实时刷表 |
| **Tor 匿名模式** | 开关即走 socks5h://127.0.0.1:9050，任务后自动 NEWNYM |
| **系统监控仪表盘** | psutil→SSE→ECharts，CPU / Mem / Net 即时曲线 |
| **权限矩阵编辑器** | Web 表格拖滑调 1-5 星，立即生效 |
| **报告导出** | HTML + PDF，静态 / 动态数据合并 |
| **CI/CD** | 多架构 Docker Buildx 推镜像；Fly.io tag-deploy 演示站 |
| **插件市场** | _即将上线_（v1.4 规划中） |

---

## 🖼️ 架构概览
```
┌─────────┐  上传 APK  ┌────────────┐
│ ReactUI ├──────────►│ Flask API  │──Tor/Socks──►Internet
└─▲──┬──▲─┘           └──▲─┬───▲───┘
  │WS│SSE                │Celery
  │  │                   ▼
  │  │         ┌──────────────────────┐
  │  │         │ static_worker        │
  │  │         └──────────────────────┘
  │  │                   │
  │  │                   ▼
  │  │         ┌──────────────────────┐
  │  │         │ dynamic_worker(runsc)│
  │  │         └─────────┬────────────┘
  │  │           tcpdump │ Frida
  │  │                   ▼
  │  │      pcap / hook / summary.json
```

---

## ⚡ 快速体验（本地 Docker）

```bash
git clone https://github.com/cesar699/Hunter-Z.git
cd Hunter-Z
# 首次构建，约 5–10 分钟（含 docker-android）
docker compose up -d --build
# 浏览器 → http://localhost:8000
# 默认口令：hunterz
```

---

## 🛠️ 从 0 开始部署（超细步骤）

### 1. 购买云服务器

| 云商 | 机型建议 | 说明 |
|------|----------|------|
| Tencent Cloud / 阿里云 | 2 vCPU 4 GB Ubuntu 22.04 | 需支持硬件虚拟化（gVisor） |
| AWS Lightsail | 2 vCPU 4 GB / $20 mo | 流量固定 4 TB 足够 |
| ***最低配置*** | 1 vCPU 2 GB 亦可跑，但动态分析较慢 |

### 2. 域名 & SSL（可选）

解析域名 + 配合 Caddy/Nginx 自动签证书。

### 3. 系统初始化

```bash
sudo apt update && sudo apt upgrade -y
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker $USER
sudo apt install -y docker-compose-plugin
curl -fsSL https://storage.googleapis.com/gvisor/releases/release/latest/runsc | sudo install -m755 /dev/stdin /usr/local/bin/runsc
sudo runsc install
docker run --rm --runtime=runsc hello-world
```

### 4. 克隆仓库 & 配置

```bash
git clone https://github.com/cesar699/Hunter-Z.git
cd Hunter-Z
docker compose up -d --build
```

### 5. 打 Tag 自动发布（可选）

1. 添加 GitHub Secrets:
   - `DOCKER_USER` / `DOCKER_PASS`
   - `FLY_API_TOKEN`（可选）
2. 打标签 → 自动构建镜像 + Release + Fly.io 演示站部署

```bash
git tag v1.3-beta
git push origin v1.3-beta
```

---

## 🧩 插件机制（v1.4 预告）

插件目录结构：

```
plugins/
└─ dns_blacklist/
   ├─ plugin.yaml        # 描述
   └─ main.py            # ctx in → result out
```

---

## 📜 License

[MIT](LICENSE) © 2025 Hunter-Z Authors
