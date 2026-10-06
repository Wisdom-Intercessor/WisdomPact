# Cloudflare Integration Plan — wisdomintercessor.com

Status: CHECKLIST / account-side verification pending

## Current boundary
WordPress on the existing origin remains the application/presentation origin. Cloudflare is the edge layer. Do not migrate the WordPress frontend to Pages/Workers solely because Git integration is available.

## Verify in Cloudflare dashboard
- Zone: wisdomintercessor.com
- DNS: apex (@) and www records point to the intended origin
- Proxy status: intended records proxied where appropriate
- SSL/TLS: end-to-end HTTPS and origin certificate validity
- WAF / managed rules: enabled and reviewed
- Cache rules: no caching of authenticated/admin/member endpoints
- Purge strategy: documented for WordPress/Elementor changes
- Workers & Pages: record whether any project currently owns the site hostname
- Git integration: only configure when a deployable GitHub project/repository is selected

## GitHub integration decision
The current repository is the WisdomPact architecture/documentation repository. It is not automatically a Cloudflare Pages deployment target. A future site-code repository should be created only when the frontend/deployment model is finalized.

## Acceptance criteria
1. DNS resolves through Cloudflare.
2. HTTPS is valid from browser to origin.
3. WordPress admin/member routes are not accidentally cached.
4. WAF does not block legitimate WordPress/Elementor operations.
5. A documented GitHub→deployment path exists before automatic production deployment is enabled.
