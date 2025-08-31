<h1 id="initializing">
    <a class="header" href="#initializing">Initializing the SDK</a>
    <a class="tag" target="_blank" href="https://breez.github.io/spark-sdk/breez_sdk_spark/struct.BreezSdk.html#method.connect">API docs</a>
</h1>

## Basic Initialization

The easiest way to initialize the SDK is with the `connect` method. This method requires:
- The network, mnemonic, and Breez API key you intend to use  
- A storage directory path where the SDK can manage its data  

<div class="warning">
<h4>Developer note</h4>
For WASM Web, SDK storage is managed using IndexedDB.
</div>

The storage is used to persist the SDK’s state. If you run multiple SDK instances, each must have its own unique storage directory.

Once connected, you’re ready to start interacting with the SDK.

<custom-tabs category="lang">
<div slot="title">Rust</div>
<section>

```rust,ignore
{{#include ../../snippets/rust/src/getting_started.rs:init-sdk}}
```

</section>

<div slot="title">Swift</div>
<section>

```swift,ignore
{{#include ../../snippets/swift/BreezSdkSnippets/Sources/GettingStarted.swift:init-sdk}}
```

</section>

<div slot="title">Kotlin</div>
<section>

```kotlin,ignore
{{#include ../../snippets/kotlin_mpp_lib/shared/src/commonMain/kotlin/com/example/kotlinmpplib/GettingStarted.kt:init-sdk}}
```

</section>

<div slot="title">Javascript</div>
<section>

```typescript
{{#include ../../snippets/wasm/getting_started.ts:init-sdk}}
```

</section>

<div slot="title">Python</div>
<section>

```python,ignore 
{{#include ../../snippets/python/src/getting_started.py:init-sdk}}
```
</section>
</custom-tabs>

<div class="warning">
<h4>Developer note</h4>

On some platforms (e.g., Android, iOS), you must use an application-specific writable directory within the app’s sandbox for SDK storage.

</div>

## Advanced Initialization

For advanced use cases where you need more control, you can configure the SDK using the Builder pattern. With the SDK Builder you can define:
- Custom storage management (bring your own implementation)
- Which chain service to use (custom or the SDK’s default)
- Which REST client to use for LNURL requests (custom or the SDK’s default)

<custom-tabs category="lang">
<div slot="title">Rust</div>
<section>

```rust,ignore
{{#include ../../snippets/rust/src/getting_started.rs:init-sdk-advanced}}
```

</section>

<div slot="title">Swift</div>
<section>

```swift,ignore
{{#include ../../snippets/swift/BreezSdkSnippets/Sources/GettingStarted.swift:init-sdk-advanced}}
```

</section>

<div slot="title">Kotlin</div>
<section>

```kotlin,ignore
{{#include ../../snippets/kotlin_mpp_lib/shared/src/commonMain/kotlin/com/example/kotlinmpplib/GettingStarted.kt:init-sdk-advanced}}
```

</section>

<div slot="title">Javascript</div>
<section>

```typescript
{{#include ../../snippets/wasm/getting_started.ts:init-sdk-advanced}}
```

</section>

<div slot="title">Python</div>
<section>

```python,ignore 
{{#include ../../snippets/python/src/getting_started.py:init-sdk-advanced}}
```
</section>
</custom-tabs>

<h2 id="disconnecting">
    <a class="header" href="#disconnecting">Disconnecting</a>
    <a class="tag" target="_blank" href="https://breez.github.io/spark-sdk/breez_sdk_spark/struct.BreezSdk.html#method.disconnect">API docs</a>
</h2>

When you’re done using the SDK, call the disconnect method to release any resources in use.

This is particularly useful if you need to re-instantiate the SDK, such as when changing the mnemonic or updating configuration.

<custom-tabs category="lang">
<div slot="title">Rust</div>
<section>

```rust,ignore
{{#include ../../snippets/rust/src/getting_started.rs:disconnect}}
```

</section>

<div slot="title">Swift</div>
<section>

```swift,ignore
{{#include ../../snippets/swift/BreezSdkSnippets/Sources/GettingStarted.swift:disconnect}}
```

</section>

<div slot="title">Kotlin</div>
<section>

```kotlin,ignore
{{#include ../../snippets/kotlin_mpp_lib/shared/src/commonMain/kotlin/com/example/kotlinmpplib/GettingStarted.kt:disconnect}}
```

</section>

<div slot="title">Javascript</div>
<section>

```typescript
{{#include ../../snippets/wasm/getting_started.ts:disconnect}}
```

</section>

<div slot="title">Python</div>
<section>

```python,ignore 
{{#include ../../snippets/python/src/getting_started.py:disconnect}}
```
</section>
</custom-tabs>
