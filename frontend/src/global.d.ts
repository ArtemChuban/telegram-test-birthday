interface TelegramBottomButton {
  text: string
  isVisible: boolean
  show: () => TelegramBottomButton
  hide: () => TelegramBottomButton
  enable: () => TelegramBottomButton
  onClick: (callback: () => void) => TelegramBottomButton
  offClick: (callback: () => void) => TelegramBottomButton
  setText: (text: string) => TelegramBottomButton
}

interface TelegramInitData {
  start_param?: string
}

interface TelegramWebApp {
  initData: string
  initDataUnsafe: TelegramInitData
  MainButton: TelegramBottomButton
  openTelegramLink: (url: string) => void
}

interface Window {
  Telegram: {
    WebApp: TelegramWebApp
  }
}
