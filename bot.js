const {
    log,
    ScanStatus,
    Wechaty
  } = require('wechaty')
  
  const bot = new Wechaty({
    name: 'ding-dong-bot',
    puppet: 'wechaty-puppet-service',
    puppetOptions: {
      tls: {
        disable: true
      },
      token: "puppet_paimon_YOUR_TOKEN" // !!!!! Please change it !!!!!
    }
  })
  
  function onScan(qrcode, status) {
    if (status === ScanStatus.Waiting && qrcode) {
      const qrcodeImageUrl = [
        'https://wechaty.js.org/qrcode/',
        encodeURIComponent(qrcode),
      ].join('')
  
      log.info('StarterBot', 'onScan: %s(%s) - %s', ScanStatus[status], status, qrcodeImageUrl)
    } else {
      log.info('StarterBot', 'onScan: %s(%s)', ScanStatus[status], status)
    }
  }
  
  function onLogin(user) {
    log.info('StarterBot', '%s login', user);
  }
  
  function onLogout(user) {
    log.info('StarterBot', '%s logout', user);
  }
  
  function onMessage(msg) {
    console.log(msg)
    if (msg.self()) return;
  }
  
  bot.on('scan', onScan)
  bot.on('login', onLogin)
  bot.on('logout', onLogout)
  bot.on('message', onMessage)
  
  bot.start()
    .then(() => {
      log.info('StarterBot', 'Starter Bot Started.');
    })
    .catch(e => {
      log.error('StarterBot', e);
    })