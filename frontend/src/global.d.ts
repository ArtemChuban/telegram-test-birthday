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

interface TelegramBackButton {
  onClick: (callback: () => void) => TelegramBackButton
  offClick: (callback: () => void) => TelegramBackButton
  show: () => TelegramBackButton
  hide: () => TelegramBackButton
}

interface TelegramInitData {
  start_param?: string
}

interface TelegramWebApp {
  initData: string
  initDataUnsafe: TelegramInitData
  MainButton: TelegramBottomButton
  SecondaryButton: TelegramBottomButton
  BackButton: TelegramBackButton
  openTelegramLink: (url: string) => void
}

interface Window {
  Telegram: {
    WebApp: TelegramWebApp
  }
}
