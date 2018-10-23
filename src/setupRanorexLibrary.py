import clr


def importDlls(pathToRanorex):
    clr.AddReference('System.Windows.Forms')

    clr.AddReferenceToFileAndPath(pathToRanorex + "\\Ranorex.Bootstrapper.dll")
    clr.AddReferenceToFileAndPath(pathToRanorex + "\\Ranorex.Contracts.dll")
    clr.AddReferenceToFileAndPath(pathToRanorex + "\\Ranorex.Controls.dll")
    clr.AddReferenceToFileAndPath(pathToRanorex + "\\Ranorex.Core.dll")
    clr.AddReferenceToFileAndPath(pathToRanorex + "\\Ranorex.Core.Resolver.dll")
    clr.AddReferenceToFileAndPath(pathToRanorex + "\\Ranorex.Core.Injection.dll")
    clr.AddReferenceToFileAndPath(pathToRanorex + "\\Ranorex.Core.WinAPI.dll")

    clr.AddReferenceToFileAndPath(pathToRanorex + "\\Ranorex.Plugin.Cef.dll")
    clr.AddReferenceToFileAndPath(pathToRanorex + "\\Ranorex.Plugin.CefHost.dll")
    clr.AddReferenceToFileAndPath(pathToRanorex + "\\Ranorex.Plugin.ChromeWeb.dll")
    clr.AddReferenceToFileAndPath(pathToRanorex + "\\Ranorex.Plugin.FirefoxWeb.dll")
    clr.AddReferenceToFileAndPath(pathToRanorex + "\\Ranorex.Plugin.Flex.dll")
    clr.AddReferenceToFileAndPath(pathToRanorex + "\\Ranorex.Plugin.Java.dll")
    clr.AddReferenceToFileAndPath(pathToRanorex + "\\Ranorex.Plugin.Mobile.dll")
    clr.AddReferenceToFileAndPath(pathToRanorex + "\\Ranorex.Plugin.Msaa.dll")
    clr.AddReferenceToFileAndPath(pathToRanorex + "\\Ranorex.Plugin.Office.dll")
    clr.AddReferenceToFileAndPath(pathToRanorex + "\\Ranorex.Plugin.Qt.dll")
    clr.AddReferenceToFileAndPath(pathToRanorex + "\\Ranorex.Plugin.RawText.dll")
    clr.AddReferenceToFileAndPath(pathToRanorex + "\\Ranorex.Plugin.Sap.dll")
    clr.AddReferenceToFileAndPath(pathToRanorex + "\\Ranorex.Plugin.Uia.dll")
    clr.AddReferenceToFileAndPath(pathToRanorex + "\\Ranorex.Plugin.Web.dll")
    clr.AddReferenceToFileAndPath(pathToRanorex + "\\Ranorex.Plugin.WebDriver.dll")
    clr.AddReferenceToFileAndPath(pathToRanorex + "\\Ranorex.Plugin.Win32.dll")
    clr.AddReferenceToFileAndPath(pathToRanorex + "\\Ranorex.Plugin.Winforms.dll")
    clr.AddReferenceToFileAndPath(pathToRanorex + "\\Ranorex.Plugin.WinformsProxy.dll")
    clr.AddReferenceToFileAndPath(pathToRanorex + "\\Ranorex.Plugin.Wpf.dll")
    clr.AddReferenceToFileAndPath(pathToRanorex + "\\Ranorex.Plugin.WpfProxy.dll")