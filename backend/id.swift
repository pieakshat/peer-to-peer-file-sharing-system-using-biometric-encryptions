import LocalAuthentication
import Foundation

func waitForBiometricAuthentication() {
    let context = LAContext()
    var error: NSError?

    
    if context.canEvaluatePolicy(.deviceOwnerAuthenticationWithBiometrics, error: &error) {
        print("Place your finger on the Touch ID sensor...")

        // biometric authentication
        context.evaluatePolicy(.deviceOwnerAuthenticationWithBiometrics, localizedReason: "Authenticate to proceed") { success, authenticationError in
            if success {
                print("Authentication successful")
                exit(0)  //  success
            } else {
                print("Authentication failed: \(authenticationError?.localizedDescription ?? "Unknown error")")
                exit(1)  //  failure
            }
        }

        // Keep the process alive until the authentication completes
        RunLoop.current.run()
    } else {
        print("Biometric authentication is not available: \(error?.localizedDescription ?? "Unknown error")")
        exit(2)  // Exit with code indicating biometrics are unavailable
    }
}

waitForBiometricAuthentication()
